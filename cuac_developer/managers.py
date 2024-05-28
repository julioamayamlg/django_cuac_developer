from django.db.models import Manager, Q
from django.db.models.query import QuerySet



class BatchMixin:
    def q_for_search_word(self, word):
        return Q(name__icontains=word) | \
               Q(created__icontains=word)

    def q_for_search(self, search):
        q = Q()
        if search:
            searches = search.split()
            for word in searches:
                q = q & self.q_for_search_word(word)

        return q

    def filter_on_search(self, search):
        return self.filter(self.q_for_search(search))


class BatchQuerySet(QuerySet, BatchMixin):
    pass


class BatchManager(Manager, BatchMixin):
    def get_queryset(self):
        return BatchQuerySet(self.model, using=self._db)


class TaskMixin:
    def q_for_search_word(self, word):
        return Q(title__icontains=word) | \
               Q(description__icontains=word)

    def q_for_search(self, search):
        q = Q()
        if search:
            searches = search.split()
            for word in searches:
                q = q & self.q_for_search_word(word)

        return q

    def filter_on_search(self, search):
        return self.filter(self.q_for_search(search))


class TaskQuerySet(QuerySet, TaskMixin):
    pass


class TaskManager(Manager, TaskMixin):
    def get_queryset(self):
        return BatchQuerySet(self.model, using=self._db)
