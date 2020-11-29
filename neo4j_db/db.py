from neo4j import GraphDatabase


class DB(object):
    ALL = 0
    NO_LABEL = None

    def __init__(self, uri, user, password):
        self.graphdb = GraphDatabase.driver(uri, auth=(user, password))
        self.session = self.graphdb.session()

    def createConnection(self, connection, labelNode1=None, labelNode2=None, propertiesNode1={}, propertiesNode2={}):
        q = "MATCH (a"
        if labelNode1 is not None:
            q += (":" + labelNode1)
        q += "), (b"
        if labelNode2 is not None:
            q += (":" + labelNode2)
        q += ")"
        if len(propertiesNode1) > 0 and len(propertiesNode2) > 0:
            q += " WHERE"
            i = 0
            if len(propertiesNode1) > 0:
                for key in propertiesNode1.keys():
                    if i != 0:
                        q += " AND"
                    q += (" a." + key + " = ")
                    if type(propertiesNode1[key]) == int:
                        q += str(propertiesNode1[key])
                    else:
                        q += ("'" + str(propertiesNode1[key]) + "'")
                    i += 1
            if len(propertiesNode2) > 0:
                for key in propertiesNode2.keys():
                    if i != 0:
                        q += " AND"
                    q += (" b." + key + " = ")
                    if type(propertiesNode2[key]) == int:
                        q += str(propertiesNode2[key])
                    else:
                        q += ("'" + str(propertiesNode2[key]) + "'")
                    i += 1
        q += " CREATE (a)-[: " + connection + "]->(b) RETURN a, b"
        return self.session.run(q)

    def createNode(self, label=None, properties={}):
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
        q += ") RETURN (N)"

        return self.session.run(q)

    def deleteNodes(self, label=None, properties={}):
        q = "MATCH (N"
        if label is not None:
            q += (":" + label)
        if len(properties) > 0:
            i = 0
            for key in properties.keys():
                if i == 0:
                    q += " {"
                else:
                    q += ", "
                q += (str(key) + ":")
                if type(properties[key]) == int:
                    q += str(properties[key])
                else:
                    q += ("'" + str(properties[key]) + "'")
                i += 1
            q += "}"
        q += ") detach delete (N)"
        return self.session.run(q)

    def getConnection(self, connection, properties={}):
        q = "MATCH (N"
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
        q += (")-[:" + connection + "]->(something) with N, something RETURN N, something")

        return self.session.run(q)

    def getCountConnections(self, connection, properties={}):
        q = "MATCH (N"
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
        q += (
                ")-[:" + connection + "]->(something) with N, count(something) AS connection_count RETURN connection_count, N"
        )

        return self.session.run(q)

    def selectNodes(self, limit=0, label=None, where={}):
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

        return self.session.run(q)
