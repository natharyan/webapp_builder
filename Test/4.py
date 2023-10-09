from pywebio.input import *
from pywebio.output import *

put_table([
    ['Name', 'Hobbies'],
    ['Tom', put_scope('hobby', content=put_text('Coding'))]  # hobby is initialized to coding
])

with use_scope('hobby', clear=True):
    put_text('Movie')  # hobby is reset to Movie

# append Music, Drama to hobby
with use_scope('hobby'):
    put_text('Music')
    put_text('Drama')

# insert the Coding into the top of the hobby
put_markdown('**Codings**', position=0)