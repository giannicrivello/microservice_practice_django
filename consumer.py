# amqps://aiimmbpf:***@beaver.rmq.cloudamqp.com/aiimmbpf  
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

params = pika.URLParameters('amqps://aiimmbpf:99CmvXDsq5Rm5_YWpK3jRkDKGeWHpLaZ@beaver.rmq.cloudamqp.com/aiimmbpf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='core')

def callback(ch, method, properties, body):
    print('recive in admin')
    print(body)
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='core', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()


# import pika


# from products.models import Product

# params = pika.URLParameters('amqps://aiimmbpf:99CmvXDsq5Rm5_YWpK3jRkDKGeWHpLaZ@beaver.rmq.cloudamqp.com/aiimmbpf')

# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# channel.queue_declare(queue='admin')


# def callback(ch, method, properties, body):
#        print('recive in admin')
#        print(body)



# channel.basic_consume(queue='admin', on_message_callback=callback)

# print('Started Consuming')

# channel.start_consuming()

# channel.close()