class index:
    def __init__(self):
        self.index = defaultdict(set)
        self.docs = {}

    def clean_text(self, text: str) -> str:
        text = re.sub(r"[#*`\[\]()>_~]", " ", text)
        return text.lower()
    def add_document(self, name, content):
        self.docs[name] = content
        cleaned = self.clean_text(content)
        for word in cleaned.split():
            self.index[word].add(name)