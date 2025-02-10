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

        public ProductsController(IProductService productService)
        {
            _productService = productService;
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

        [HttpPost]
        public async Task<IActionResult> CreateProduct([FromBody] JsonElement productJson)
        {
            // Deserialize the JsonElement to a Product
            Product? product;

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
    }
}