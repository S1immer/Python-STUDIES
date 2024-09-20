class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0


    def upvote(self):
        self.votes_qty += 1


first_comment = Comment("First comment")
print(first_comment.__dict__)
# {'text': 'First comment', 'votes_qty': 0}

print(first_comment.text)
# First comment

print(first_comment.votes_qty)
# 0
# _______________________________________________




