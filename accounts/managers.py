from django.contrib.auth.base_user import BaseUserManager


class UserRegistrationInfoMangers(BaseUserManager):

    def create_user(self, first_name, last_name, customer_email, password, customer_phone, **extra_fields):

        if not customer_email:
            raise ValueError("Please Provide An Email Address")
        if not customer_phone:
            raise ValueError("Please Provide A Phone Number")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            customer_email=self.normalize_email(customer_email),
            password=password,
            customer_phone=customer_phone,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, customer_email, password, customer_phone, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(first_name, last_name, customer_email, password, customer_phone, **extra_fields)