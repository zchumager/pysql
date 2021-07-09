import itertools


def select_post_by_user_id(posts, user_id) -> list:
    return list(filter(lambda post: post['userId'] == user_id, posts))


def select_user_by_email_domain(users, domain) -> list:
    return list(filter(lambda user: domain in user['email'], users))


def inner_join(table_and_field_a, table_and_field_b) -> list:

    cartesian_product = itertools.product(table_and_field_a[0], table_and_field_b[0])

    '''
        itertools.product returns a list of tuples with all the cartesian product
    '''
    return list(
        filter(lambda record: record[0][table_and_field_a[1]] == record[1][table_and_field_b[1]], cartesian_product)
    )


def complex_inner_join(*args):
    # do not use list as fn because it change the nature of expected result
    collections = (list)(map(lambda collection: collection[0], args))

    cartesian_product = itertools.product(collections[0], collections[1], collections[2])

    # creating an array with the elements to be used by the lambda expression below
    lambda_elements = [f"record[{index}]['{args[index][1]}']" for index in range(len(args))]

    # creating the proper expression to be executed by eval fn
    lambda_expression = generate_lambda_expression(lambda_elements)

    return (list)(filter(lambda record: eval(lambda_expression), cartesian_product))


def generate_lambda_expression(lambda_elements) -> str:
    '''

    needs to put key inside double quotes
    '''

    expression = ""
    limit = len(lambda_elements) - 1

    for index in range(limit):
        expression = expression + f"{lambda_elements[index]} == {lambda_elements[index + 1]}"
        if index < limit - 1:
            expression = expression + " and "

    return expression
