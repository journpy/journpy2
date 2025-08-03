from ..base_model import BaseTutorial


class LearnDjango(BaseTutorial):
    """ Model a Django tutorial. """

    class Meta:
        verbose_name = 'Django Tutorial'
        verbose_name_plural = 'Django Tutorial'
        ordering = ('-date_created',)


    def __str__(self):
        """ Return a string representation of LearnDjango object."""
        return self.title.title()


