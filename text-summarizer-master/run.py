import nltk
import text_summarizer


class base_summarize :
    def __init__(self):
        # prepare nltk data
        nltk.download('punkt')
        nltk.download('stopwords')
        
    def summarize(self,text_tobe_summarized):
        


        #text = ""

        # we'll need embedding model from gensim for summarizer
        # this can take a while
        embedding_model = text_summarizer.centroid_word_embeddings.load_gensim_embedding_model('glove-wiki-gigaword-50')

        centroid_word_embedding_summarizer = text_summarizer.CentroidWordEmbeddingsSummarizer(embedding_model, preprocess_type='nltk')

        centroid_word_embedding_summary = centroid_word_embedding_summarizer.summarize(text_tobe_summarized)
        summarized_text = centroid_word_embedding_summarizer.summarize(text_tobe_summarized)
        #print(summarized_text)
        return summarized_text
#g = base_summarize()
#f = g.summarize("Japan, which aimed to dominate Asia and the Pacific, was at war with China by 1937,[5][b] though neither side had declared war on the other. World War II is generally said to have begun on 1 September 1939,[7] with the invasion of Poland by Germany and subsequent declarations of war on Germany by France and the United Kingdom. From late 1939 to early 1941, in a series of campaigns and treaties, Germany conquered or controlled much of continental Europe, and formed the Axis alliance with Italy and Japan. Under the Molotov–Ribbentrop Pact of August 1939, Germany and the Soviet Union partitioned and annexed territories of their European neighbours, Poland, Finland, Romania and the Baltic states. Following the onset of campaigns in North Africa and East Africa, and the Fall of France in mid 1940, the war continued primarily between the European Axis powers and the British Empire. War in the Balkans, the aerial Battle of Britain, the Blitz, and the long Battle of the Atlantic followed. On 22 June 1941, the European Axis powers launched an invasion of the Soviet Union, opening the largest land theatre of war in history. This Eastern Front trapped the Axis, most crucially the German Wehrmacht, in a war of attrition. In December 1941, Japan launched a surprise attack on the United States as well as European colonies in the Pacific. Following an immediate U.S. declaration of war against Japan, supported by one from Great Britain, the European Axis powers quickly declared war on the U.S. in solidarity with their Japanese ally. Rapid Japanese conquests over much of the Western Pacific ensued, perceived by many in Asia as liberation from Western dominance and resulting in the support of several armies from defeated territories.")
#print(f)