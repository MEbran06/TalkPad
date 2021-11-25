from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import true
from .. import schemas, database, models, oauth2

router = APIRouter(
    prefix = "/like",
    tags=['like']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def like(like: schemas.like, db: Session = Depends(database.get_db), current_user: int = Depends
(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == like.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f'Post with id: {like.post_id} does not exist')

    like_query = db.query(
        models.Like).filter(models.Like.post_id == like.post_id, models.Like.user_id == current_user.id)

    found_like = like_query.first() 

    if (like.dir == True):
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail= f"user {current_user.id} has already liked a post {like.post_id}")
        new_vote = models.Like(post_id = like.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message": "like added"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        like_query.delete(synchronize_session=False)
        db.commit()
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)



