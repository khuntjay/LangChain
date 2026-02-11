from langchain_community.document_loaders import   WebBaseLoader

url = 'https://www.amazon.com/Apple-2025-MacBook-Laptop-10%E2%80%91core/dp/B0FWD6SKL6/ref=sr_1_1_sspa?crid=1KXY7U1YJWH2L&dib=eyJ2IjoiMSJ9.UtbcVQ6umCJbRtFCQ0GpnrZSsoeudCDt_lIMl7kwiZ4m_FjSJq4qELL-hhXiorkNHZ2_FW1o4HV4PNruHTB1G3C38El1cZMkU4NlNFB8gqk4F8Pdtyaet0OXb4ic-itMTfAAymi3GeQlAWJmR4AQz0NuOGNWyCLWNJpKC6Gzp25b9OfPUdXBWzP5Ntj_mlQtqbXptTdEW6vWz4VLRYtp5hf4dCBWHyPMKM_CYZ-xzMc.B-q2mQbwxHxMSrh1xE9FjliYDDC5Qh7UG6PXe-flJsM&dib_tag=se&keywords=macbook%2Bpro&qid=1770780956&sprefix=macbook%2B%2Caps%2C151&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'


loader  = WebBaseLoader(url)
docs = loader.load()

print(docs[0].page_content)