namespace PriceScraperApi.Services;

public interface IRabbitMqService
{
    Task SendMessageAsync<T>(T message, string queueName);
}