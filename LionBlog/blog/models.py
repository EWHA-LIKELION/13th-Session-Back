from django.db import models
from django.utils import timezone #댓글 생성 시간을 나타내기 위한 import

# Create your models here.

class Hashtag(models.Model) :
  hashtag = models.CharField(max_length=100)

  def __str__(self):
    return self.hashtag
  
class Post(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateTimeField('data published')
  body = models.TextField()
  hashtag = models.ManyToManyField(Hashtag)
  photo = models.ImageField(blank = True, null = True, upload_to = "post_photo")

  def __str__(self):
    return self.title
  
  def summary(self):
    return self.body[:100]

  
class Comment(models.Model): #post와 1:N 관계인 모델 작성
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE) 
  #ForeignKey: 데이터베이스에서 다른 테이블을 참조하기 위해 사용. 중복되지 않는 고유한 값.
  #related_name(역참조): Post 모델에서 댓글에 접근할 수 있게 함
  #on_delete: ForeignKey가 참조하는 데이터가 삭제(CASCADE) 되었을 때 해당 요소를 처리하는 방법을 명시 (게시물이 삭제되면 댓글도 삭제되어야 함)
  username = models.CharField (max_length=20)
  comment_text = models.TextField()
  created_at = models.DateTimeField (default=timezone.now)
  #default: 기본 시간을 설정
                                                            
  def approve(self):
    self.save()

  def _str_(self):
      return self.comment_text
  
