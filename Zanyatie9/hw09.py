__author__ = 'Вершинин Иван Александрович'


class Tag:
    tag_name = None
    tag_template = '<{tag_name}></{tag_name}>'

    @classmethod
    def create_tag(cls, tag_name, tag_template=None):
        self = cls()
        self.tag_name = tag_name
        if tag_template is not None:
            self.tag_template = tag_template
        return self

    def __repr__(self):
        return self.tag_template.format(tag_name=self.tag_name)


class Div(Tag):
    tag_name = 'div'


if __name__ == '__main__':
    d = Div()
    print(Tag.create_tag('span'))
    print(d)