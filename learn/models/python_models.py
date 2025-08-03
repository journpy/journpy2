from ..base_model import BaseTutorial


class LearnPython(BaseTutorial):
    """ Model a Python tutorial. """

    class Meta:
        verbose_name = 'Python Tutorial'
        verbose_name_plural = 'Python Tutorial'
        ordering = ('-date_created',)


    def __str__(self):
        """ Return a string representation of LearnPython object."""
        return self.title.title()


