using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.Testing;
using PriceScraperApi.Models;
using Xunit;

namespace PriceScraperApi.Tests;

public class BenchmarkTests : IClassFixture<WebApplicationFactory<Program>>
    {
        private readonly HttpClient _client;

        public BenchmarkTests(WebApplicationFactory<Program> factory)
        {
            _client = factory.CreateClient();
        }

        [Fact]
        public async Task GetRunningTime()
        {
            var products = await _client.GetFromJsonAsync<List<Product>>("/Products");
            Assert.NotNull(products);
            Assert.NotEmpty(products);

            // Order products by timestamp and calculate the elapsed time.
            var orderedProducts = products.OrderBy(p => p.Timestamp).ToList();
            var firstTimestamp = orderedProducts.First().Timestamp;
            var lastTimestamp = orderedProducts.Last().Timestamp;
            var totalDuration = lastTimestamp - firstTimestamp;

            Console.WriteLine("Total elapsed time between first and last product: " + totalDuration);
        }
        
        [Fact]
        public async Task Benchmark_SendProducts_And_CreateProducts()
        {
            // Create 10 product names for SendProductsToQueue endpoint.
            var productNames = new List<string>
            {
                "Chicken",
                "Beef",
                "Milk",
                "Eggs",
                "Bread",
                "Cheese",
                "Butter",
                "Yogurt",
                "Apples",
                "Tomatoes"
            };
            
            // Save a fake product in the DB just to have a timestamp.
            var fakeProduct = new Product
            {
                Name = "Fake Product",
                Price = 10.0m,
                PricePerKg = 1.0m,
                Timestamp = DateTime.UtcNow
            };
            var fakePayload = new List<Product> { fakeProduct };
            var fakeResponse = await _client.PostAsJsonAsync("/Products/create-products", fakePayload);
            fakeResponse.EnsureSuccessStatusCode();

            var sendProductsToQueue = await _client.PostAsJsonAsync("/Products/send-products", productNames);
            sendProductsToQueue.EnsureSuccessStatusCode();
            
            // Wait for 2 minutes to allow additional products to be processed.
            await Task.Delay(TimeSpan.FromMinutes(1));

            // Retrieve all products from the DB via the GET endpoint (assumed route: /Products).
            var products = await _client.GetFromJsonAsync<List<Product>>("/Products");
            Assert.NotNull(products);
            Assert.NotEmpty(products);

            // Order products by timestamp and calculate the elapsed time.
            var orderedProducts = products.OrderBy(p => p.Timestamp).ToList();
            var firstTimestamp = orderedProducts.First().Timestamp;
            var lastTimestamp = orderedProducts.Last().Timestamp;
            var totalDuration = lastTimestamp - firstTimestamp;

            Console.WriteLine("Total elapsed time between first and last product: " + totalDuration);
            
            

            
        }
    }