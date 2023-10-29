from django.shortcuts import get_object_or_404, redirect, render
from conversations.forms import ConversationMessageForm
from conversations.models import Conversation
from listings.models import ads
from accounts.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/sign_in/')
def inbox(request):
    conversations = Conversation.objects.filter(user_members__in=[request.user.uid])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required(login_url='/sign_in/')
def new_conversation(request, adsid):
    item = get_object_or_404(ads, pk=adsid)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=adsid)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required(login_url='/sign_in/')
def detail(request, pk):
    userDetails = User.objects.get(email=request.user)

    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'data': userDetails
    })