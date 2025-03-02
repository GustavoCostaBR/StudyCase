using PriceScraperApi.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PriceScraperApi.Repositories
{
    public interface IProductRepository
    {
        Task<Product> GetProduct(string id);
        Task<IEnumerable<Product>> GetAllProducts();
        Task CreateProduct(Product product);
        Task CreateProducts(IEnumerable<Product> products);
    }
}