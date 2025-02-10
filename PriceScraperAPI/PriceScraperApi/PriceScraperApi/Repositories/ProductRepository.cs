using PriceScraperApi.Models;
using MongoDB.Driver;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace PriceScraperApi.Repositories
{
    public class ProductRepository : IProductRepository
    {
        private readonly IMongoCollection<Product> _products;

        public ProductRepository(IMongoDatabase database)  // Inject IMongoDatabase
        {
            _products = database.GetCollection<Product>("Products");
        }

        public async Task<Product> GetProduct(string id)
        {
            return await _products.Find(p => p.Id == id).FirstOrDefaultAsync();
        }

        public async Task<IEnumerable<Product>> GetAllProducts()
        {
            return await _products.Find(_ => true).ToListAsync();
        }

        public async Task CreateProduct(Product product)
        {
            await _products.InsertOneAsync(product);
        }
    }
}