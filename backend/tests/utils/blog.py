from http.client import responses

from sqlalchemy.orm import Session
from db.repository.blog import create_new_blog
from schemas.blog import CreateBlog
from tests.utils.user import create_random_user
from tests.utils.blog import create_random_blog


def create_random_blog(db: Session):
    blog = CreateBlog(title="first_blog", content="Tests make the system stable!")
    user = create_random_user(db=db)
    blog = create_new_blog(blog=blog, db=db, author_id=user.id)
    return blog


def test_should_fetch_blog_created(client, db_session):
    blog = create_random_blog(db=db_session)
    # print(blog.__dict__)  # pytest -s чтобы увидеть операторы печати
    response = client.get(f"blog/{blog.id}/")
    assert response.status_code == 200
    assert response.json()["title"] == blog.title

