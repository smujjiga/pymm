# Python Wrapper for MetaMap

Python Wrapper for extracting candidate and mapping concepts using MetaMap. The below concept information are extracted:
*   score
*   matched word
*   cui
*   semtypes

The flag <code>ismapping</code> is set to True if it is a mapping concept else it is False for a candidate mapping.

## Installation

<pre><code>
git clone https://github.com/smujjiga/pymm.git
cd pymm
python setup.py install
</code></pre>


## Usage
Create Python MetaMap wrapper object by pointing it to locaiton of MetaMap

<pre><code>
mm = Metamap(METAMAP_PATH)
</code></pre>

We can check if metamap is running using
<pre><code>
assert mm.is_alive()
</code></pre>

Concept extraction is done via parse method
<pre><code>
mmos = mm.parse(['heart attack', 'mayocardia infarction'])
</code></pre>

Parse method returns an iterator of Metamap Objects iterators corresponding to each input sentence. Each Metamap Objects iterator return the candidate and mapping concepts.
<pre><code>
for idx, mmo in enumerate(mmos):
   for jdx, concept in enumerate(mmo):
     print (concept.cui, concept.score, concept.matched0
     print (concept.semtypes, concept.ismapping)
</code></pre>
Python MetaMap wrapper object also support debug parameter which persists input and output file as well print the command line used to run the MetaMap
