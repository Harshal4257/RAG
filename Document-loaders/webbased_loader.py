from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.amazon.in/Red-Tape-Elegantly-Soothing-Impact-Resistant/dp/B0FHDD75FQ/ref=sr_1_1?crid=6PKM4D87IKQU&dib=eyJ2IjoiMSJ9.KLkmfbfTcSrhCVyrjyIXszbddOIWc3ErV6ZGYDtwIJNYtzOVwojjjy_3ecGa_Jq3K5g_Llg7IZhSIsso3SrV7N5LDp-4HPwvVtxsRv4LjoKxfRN8Y3Qdw_q4mbGTOIm7GmCArtF2q60UVJQcHswzZ_hzDWS6-wOT9mOPoH_XeEtEQpC8G4pPkeCqE6Fhmgm1uDnejs15xZvuKnnEn5M8c0kqqmxpmOppQ09pEqjX1_3O-7C4t5RssaHHLcl4EPILvx0dDTjYeK9uo3fSl30CwQAWgGeiucH_ZBKvzuOGljw.DdlXyKfwL_k-nBs6iQks50WOGgXdpRctw5gPE1_6poc&dib_tag=se&keywords=redtape%2Bsneakers%2Bfor%2Bman&qid=1789972500&sbm=true&setroute=search&sprefix=redt%2Caps%2C334&sr=8-1&th=1&psc=1'
loader = WebBaseLoader(url)

docs = loader.load()
print(docs[0].page_content)