import requests

from pprint import pprint
from utils.string_utils import print_separator
from pysql.queries import \
    select_post_by_user_id, select_user_by_email_domain, inner_join, complex_inner_join


def main():
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()

    print_separator("select posts by id")
    selected_post = select_post_by_user_id(posts, 1)
    pprint(selected_post)

    print_separator("select users by email domain")
    selected_users = select_user_by_email_domain(users, ".biz")
    pprint(selected_users)

    print_separator("inner join")
    inner_list = inner_join((users, "id"), (posts, "userId"))
    pprint(inner_list)

    print_separator("complex inner join")
    complex_inner_list = complex_inner_join((users, "id"), (posts, "userId"), (albums, "userId"))
    pprint(complex_inner_list)


if __name__ == "__main__":
    main()
