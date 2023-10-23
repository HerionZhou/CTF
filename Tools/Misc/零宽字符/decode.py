import zwsp_steg

encoded = zwsp_steg.encode('P@‌‌‌‌‍﻿‬‍ssW0‌‌‌‌‌﻿‌‌‌‌‌‌‍﻿‍‍‌‌‌‌‍‍﻿﻿‌‌‌‌‍‬‍‬‌‌‌‌‌﻿‌‌rd_‌‌‌‌‍﻿‍‍‌‌‌‌‍‬﻿‬‌‌‌‌‍‬‍‌‌‌‌‌‍‍﻿﻿‌‌‌‌‍‬﻿‍1s‌‌‌‌‌﻿‌﻿_h3re')
decoded = zwsp_steg.decode(encoded)

print(decoded)  # hidden message