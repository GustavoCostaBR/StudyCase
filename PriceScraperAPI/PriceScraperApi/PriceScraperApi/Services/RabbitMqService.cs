using RabbitMQ.Client;
using System;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace PriceScraperApi.Services
{
    public class RabbitMqService : IRabbitMqService
    {
        private readonly ConnectionFactory _factory;

        public RabbitMqService(IConfiguration configuration)
        {
            var connectionString = configuration.GetSection("RabbitMq")["ConnectionString"];

            _factory = new ConnectionFactory()
            {
                Uri = new Uri(connectionString),
                DispatchConsumersAsync = true
            };
        }

        public async Task SendMessageAsync<T>(T message, string queueName)
        {
            Console.WriteLine($"Attempting to connect to RabbitMQ at {_factory.HostName}...");
            using var connection = _factory.CreateConnection();
            using var channel = connection.CreateModel();

            Console.WriteLine("Successfully connected to RabbitMQ!");
            
            channel.QueueDeclare(queue: queueName, durable: false, exclusive: false, autoDelete: false, arguments: null);

            var messageBody = JsonSerializer.Serialize(message);
            var body = Encoding.UTF8.GetBytes(messageBody);

            await Task.Run(() => channel.BasicPublish(exchange: "", routingKey: queueName, basicProperties: null, body: body));
            Console.WriteLine($"Message successfully sent to queue: {queueName}");
        }
    }
}