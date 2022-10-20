# ZipSubmissionsExtractor

Þegar maður sækir öll verkefnin á canvas er það ein stór zip skrá, inní þesari zip skrá eru pdf og aðrar zip skrár.
unzip_submissions.py tekur þessa zip skrá, extractar öll innri zip og pdf og flokkar þær í möppur eftir nafni nemanda.

## Hvernig á folder strúktúrinn að vera?

Segjum að við erum með folder strúktúrinn

```
|-- lab4
   |-- example_feedback_template.txt
   |-- submissions.zip
|-- unzip_submissions.py
```
Þá mun skriptan bæta við möppunni svona:
```
|-- lab4
   |-- example_feedback_template.txt
   |-- submissions.zip
   |-- submissions
      |-- studentname1
         |-- ...
      |-- studentname2
         |-- ...
      ...
      |-- studentname59
         |-- ...
|-- unzip_submissions.py
```

## Dæmi um keyrslu

Byrjum á því að keyra skriptuna
```
py ./unzip_submissions.py
```

Forritið biður þig um að slá inn möppu með submissions.zip
```
Enter the name of the lab/project folder you want to extract: lab4
```

Næst biður forritið um að bæta við feedback file fyrir hverja möppu (optional)
```
Do you want to generate from a temaplate feedback file? (y/n): y
```

Svo keyrir skriptan og gerir sitt magic

