# from django.contrib.auth.base_user import BaseUserManager


# class ListingManager(BaseUserManager):
#     use_in_migrations = True

#     def add_new_listings(self, title, **extrafields):
#         if not title:
#             raise ValueError("Title is require")

#         # email = self.normalize_email(email)
#         # user = self.model(email=email, **extrafields)
#         # user.set_password(password)
#         addListing = self.model(ads_title=title, **extrafields)
#         addListing.save(using=self._db)
#         return addListing
