from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_relay import from_global_id


class RelaySerializerMutation(SerializerMutation):
    class Meta:
        abstract = True

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        if 'client_mutation_id' in input:
            _, input['id'] = from_global_id(input['client_mutation_id'])
        return super().mutate_and_get_payload(root, info, **input)
