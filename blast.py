
from sys import argv
if len(argv)==1:
        consumer=KafkaConsumer('topic2',  bootstrap_servers=['192.168.20.199:39092','192.168.20.199:39093', '192.168.20.199:39094','192.168.20.199:9092', '192.168.20.199:9093', '192.168.20.199:9094' ])
elif len(argv)==3:
        consumer=KafkaConsumer(argv[1],  bootstrap_servers=[argv[2]]  )

def callblast(incoming, filename, database='human.1.protein.faa'):
        with open(filename, "w") as f:
                f.write(incoming)
        blst_result="blastp -query %s -db %s -evalue 1e-5 -outfmt 6 -max_target_seqs 1" %(filename,database)
        blst_resultt=os.system(blst_result)
        end = time.time()
        print("time occurred:", (end-start))
enterance=""
while True:
        entrance=''
        message = consumer.poll(timeout_ms = 1000, max_records = 500)
        if not message:
                continue
        for partition,msgs in message.items():
                for msg in msgs:
                        entrance+=(msg.value)+'\n'
        callblast(entrance, "feedfile.txt")
