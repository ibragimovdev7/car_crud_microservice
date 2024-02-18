class KafkaSettings:
    __bootstrap_servers = '127.0.0.1:9092'
    __topic = 'myTestTopic'

    @property
    def get_bootstrap_server(self):
        return self.__bootstrap_servers

    def set_bootstrap_server(self, bootstrap_servers):
        self.__bootstrap_servers = bootstrap_servers
        print('Server changed..')

    @property
    def get_topic(self):
        return self.__topic

    def set_topic(self, topic_name):
        self.__topic = topic_name
        print('Topic changed..')


kafka = KafkaSettings()
