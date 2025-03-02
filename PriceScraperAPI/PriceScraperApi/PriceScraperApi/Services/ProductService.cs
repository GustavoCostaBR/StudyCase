using PriceScraperApi.Models;
using PriceScraperApi.Repositories;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PriceScraperApi.Services
{
    public class ProductService : IProductService
    {
        private readonly IProductRepository _productRepository;

        public ProductService(IProductRepository productRepository)
        {
            _productRepository = productRepository;
        }

        public async Task<Product> GetProduct(string id)
        {
            return await _productRepository.GetProduct(id);
        }

        public async Task<IEnumerable<Product>> GetAllProducts()
        {
            return await _productRepository.GetAllProducts();
        }

        public async Task CreateProduct(Product product)
        {
            await _productRepository.CreateProduct(product);
        }
        
        public async Task CreateProducts(IEnumerable<Product> products)
        {
            await _productRepository.CreateProducts(products);
        }
    }
}