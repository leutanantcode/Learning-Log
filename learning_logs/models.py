from django.db import models
class Topic(models.Model):
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    #Each entry must be tied or associated to and with a certain topic.[this a many-one relationship]

    
class Entry(models.Model): # This class defines the kind of entries that are going to be made.
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    # . This is the code that connects each entry to a specific topic. Each topic is assigned a key, or ID, when it’s created. When Django needs to establish a connection between two pieces of data, it uses the key associated with each piece of information
    date_added = models.DateTimeField(auto_now_add = True)
    text = models.TextField(default="")
    #we nest the meta class inside this class to tell Django extra infromation on how to handle this model, in this case telling it to use entries when it refers to more than one entry.
    class Meta:
        verbose_name_plural = 'entries'
    #This method tells Django which information to show when it refers to individual entries.
    def __str__(self):
        return f"{self.text[:50]}..."