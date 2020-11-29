from neo4j_db.db import DB


class SpecialDB(DB):
    NAME_CONNECTION_WITH_COMPANY = "worksIn"

    def __init__(self, uri, user, password, company_name=None):
        super().__init__(uri, user, password)
        if company_name is not None:
            self.company_name = company_name
            self.createNode("company", {"name": company_name})

    def createConnectionEmployeeWithCompany(self, properties={}):
        return self.createConnection("worksIn", "employee", "company", properties, {"name": self.company_name})

    def createEmployee(self, name, surname, email):
        node = self.createNode("employee", {"name": name, "surname": surname, "email": email})
        self.createConnectionEmployeeWithCompany({"name": name, "surname": surname, "email": email})
        return node

    def deleteEmployees(self, properties={}):
        return self.deleteNodes("employee", properties)
