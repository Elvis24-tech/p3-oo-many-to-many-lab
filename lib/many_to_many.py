class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = [] 

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of Book")
        if not isinstance(date, str):
            raise ValueError("date must be a string")
        if not isinstance(royalties, int):
            raise ValueError("royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        filtered_contracts = [contract for contract in cls.all if contract.date == date]
        return filtered_contracts