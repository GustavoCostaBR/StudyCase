using Microsoft.AspNetCore.Mvc;
using PriceScraperApi.Models;
using PriceScraperApi.Services;
using System.Threading.Tasks;
using System.Text.Json;

namespace PriceScraperApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ProductsController : ControllerBase
    {
        private readonly IProductService _productService;
        private readonly IRabbitMqService _rabbitMqService;

        public ProductsController(IProductService productService, IRabbitMqService rabbitMqService)
        {
            _productService = productService;
            _rabbitMqService = rabbitMqService;
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetProduct(string id)
        {
            var product = await _productService.GetProduct(id);
            if (product == null)
            {
                return NotFound();
            }
            return Ok(product);
        }

        [HttpGet]
        public async Task<IActionResult> GetAllProducts()
        {
            var products = await _productService.GetAllProducts();
            return Ok(products);
        }

        [HttpPost("create-product")]
        public async Task<IActionResult> CreateProduct([FromBody] JsonElement productJson)
        {
            // Deserialize the JsonElement to a Product
            Product? product;
            
            Console.WriteLine(productJson.ToString());

            try
            {
                product = JsonSerializer.Deserialize<Product>(productJson.GetRawText());
                if (product == null)
                {
                    return BadRequest("Invalid Product data.");
                }
            }
            catch (Exception ex)
            {
                return BadRequest($"Invalid Product data: {ex.Message}");
            }

            await _productService.CreateProduct(product);
            return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
        }
        
        [HttpPost("send-products")]
        public async Task<IActionResult> SendProductsToQueue([FromBody] List<string> productNames)
        {
            if (productNames == null || productNames.Count == 0)
            {
                return BadRequest("Product names list cannot be empty.");
            }

            try
            {
                await _rabbitMqService.SendMessageAsync(productNames, "product_queue");
                return Ok("Products sent to the queue.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Failed to send products to the queue: {ex.Message}");
            }
        }
        
        [HttpPost("test-mq")]
        public async Task<IActionResult> TestRabbitMq([FromServices] IRabbitMqService rabbitMqService)
        {
            try
            {
                await rabbitMqService.SendMessageAsync("Test Message", "test_queue");
                return Ok("Message successfully sent to RabbitMQ");
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Failed to connect to RabbitMQ: {ex.Message}");
            }
        }


    }
}