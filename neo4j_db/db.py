from neo4j import GraphDatabase


class DB(object):
    ALL = 0
    NO_LABEL = None

    def __init__(self, uri, user, password, company_name):
        self.graphdb = GraphDatabase.driver(uri, auth=(user, password))
        self.session = self.graphdb.session()
        # self.create(company_name)

    def select(self, limit=0, label=None, where={}):
        q = "MATCH (x"
        if label is not None:
            q += (":" + label)
        q += ") return (x)"
        if len(where) > 0:
            i = 0
            for key in where.keys():
                if i == 0:
                    q += " where"
                else:
                    q += " and"
                q += (" x." + str(key) + "=")
                if type(where[key]) == int:
                    q += str(where[key])
                else:
                    q += ("'" + str(where[key]) + "'")
                i += 1
        if limit > 0:
            q += (" LIMIT " + str(limit))

        for node in self.session.run(q):
            print(node)

    def create(self, label=None, properties={}):
        q = "CREATE (N"
        if label is not None:
            q += (":" + label)
        if len(properties) > 0:
            i = 0
            for key in properties.keys():
                if i == 0:
                    q += "{"
                else:
                    q += ", "
                q += (str(key) + ":")
                if type(properties[key]) == int:
                    q += str(properties[key])
                else:
                    q += ("'" + str(properties[key]) + "'")
                i += 1
            q += "}"
        q += ")"

        self.session.run(q)
        self.select(self.ALL, label)
