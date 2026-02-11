from langchain_text_splitters import CharacterTextSplitter


# text which we want to split
text  = """"NASA Today
NASA explores the unknown in air and space, innovates for the benefit of humanity, and inspires the world through discovery. For more than 65 years, NASA has made the seemingly impossible, possible. At its 20 centers and facilities across the country and with U.S. commercial companies and international partners, NASA leads studying Earth science, including climate, our Sun, solar system, and the larger universe. We conduct cutting-edge research to advance technology and aeronautics. We operate the world’s leading space laboratory, the International Space Station, and will establish a sustainable and strong exploration presence on the Moon this decade through the Artemis campaign."""


# splite the text
spllitter  = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=  0,
    separator=' '
)

result  = spllitter.split_text(text)

print(result)