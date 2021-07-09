import itertools


def select_post_by_user_id(posts, user_id) -> list:
    return list(filter(lambda post: post['userId'] == user_id, posts))


def select_user_by_email_domain(users, domain) -> list:
    return list(filter(lambda user: domain in user['email'], users))


def inner_join(collection_a, field_collection_a, collection_b, field_collection_b) -> list:

    cartesian_product = itertools.product(collection_a, collection_b)

    '''
        itertools.product returns a list of tuples with all the cartesian product
    '''
    return list(
        filter(lambda record: record[0][field_collection_a] == record[1][field_collection_b], cartesian_product)
    )


def complex_inner_join(*args) -> list:
    cartesian_product = itertools.product(map(lambda collection: collection[0], args))

    #
    lambda_elements = [f"record[{index}][{args[index][1]}]" for index in range(len(args))]

    lambda_expression = generate_lamda_expression(lambda_elements)

    '''
    casting the filter result to a list 
    because list(filter(lambda record: lambda_expression, cartesian_product)) not working
    '''
    return (list)(filter(lambda record: lambda_expression, cartesian_product))


def generate_lamda_expression(lambda_elements) -> str:
    expression = ""
    limit = len(lambda_elements) - 1

    for index in range(limit):
        expression = expression + f"{lambda_elements[index]} == {lambda_elements[index + 1]}"
        if index < limit - 1:
            expression = expression + " and "

    return expression
