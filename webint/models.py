from webint import db, coh


def as_json(category):
    """Jsonify a category.
    :returns: A dictionary containing the values for all the metrics in the
        category.

    """
    d = {}
    for m in category.category.metrics:
        value = getattr(category, m.column_name)

        if isinstance(value, float) or isinstance(value, int):
            d[m.column_name] = value
        else:
            d[m.column_name] = str(value)

    return d


def from_coh_category(category):
    """Convert a Coh-Metrix-Port category into a SQLAlchemy class.

    :category: An instance of coh.base.Category
    :returns: A SQLAlchemy class suitable for storing the category to a DB.
    """
    attrs = {'__tablename__': category.table_name,
             'id': db.Column(db.Integer, primary_key=True),
             'category': category}

    for metric in category.metrics:
        attrs[metric.column_name] = db.Column(db.Float)

    C = type(category.__class__.__name__, (db.Model,), attrs)

    return C


categories = [from_coh_category(category)
              for category in coh.all_metrics.categories]


def find_category(name):
    """Find a category class using its table name.

    :name: The category's table_name.
    :returns: The corresponding class in the 'categories' list.

    """
    for category in categories:
        if category.category.table_name == name:
            return category


class Text(db.Model):
    __tablename__ = 'texts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    source = db.Column(db.String(50))
    publication_date = db.Column(db.Date)
    genre = db.Column(db.String(50))
    content = db.Column(db.String(300))

    def __init__(self, title='', author='', source='', publication_date='',
                 genre='', content=''):
        self.title = title
        self.author = author
        self.source = source
        self.publication_date = publication_date
        self.genre = genre
        self.content = content

    @staticmethod
    def from_coh_text(text):
        """Instantiate a Text object from an already initialized coh.base.Text
            object.

        :text: A coh.base.Text instance.
        :returns: A Text instance with the same attributes.

        """
        obj = Text()

        obj.title = text.title
        obj.author = text.author
        obj.source = text.source
        obj.publication_date = text.publication_date
        obj.genre = text.genre
        obj.content = text.content

        return obj

    def as_coh_text(self):
        """Instantiate a coh.base.Text object with the same attributes.
        :returns: A coh.base.Text instance with the same attributes as this one.

        """
        obj = coh.base.Text(title=self.title,
                            author=self.author,
                            source=self.source,
                            publication_date=self.publication_date,
                            genre=self.genre,
                            content=self.content)

        return obj

    def analyze(self):
        """Analyze this text through Coh-Metrix-Dementia.

        :returns: TODO

        """
        text = self.as_coh_text()
        r = coh.all_metrics.values_for_text(text)
        return str(r)
