from users.models import User

import graphene
from graphene_django import DjangoObjectType
import bcrypt


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "is_active", "created_on", "updated_on")


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self, info, id):
        return User.objects.get(id=id)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        is_active = graphene.Boolean()

    def mutate(root, info, name, email, password, is_active):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(name=name, email=email, password=hashed_password, is_active=is_active)
        user.save()

        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        is_active = graphene.Boolean()

    def mutate(root, info, id, name, email, password, is_active):
        user = User.objects.get(id=id)
        user.name = name
        user.email = email
        user.password = password
        user.is_active = is_active
        user.save()

        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int()

    def mutate(root, info, id):
        user = User.objects.get(id=id)
        user.delete()

        return None


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
