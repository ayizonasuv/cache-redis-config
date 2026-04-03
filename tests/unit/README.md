# Cache Redis Config

This project provides a configuration setup for integrating Redis as a caching layer in your application. It includes best practices for connection management, error handling, and cache invalidation.

## Features

- **Redis Connection Management**: Automatically handles connection pooling and reconnection logic.
- **Error Handling**: Gracefully handles Redis errors and provides fallback mechanisms.
- **Cache Invalidation**: Supports TTL-based and manual cache invalidation strategies.

## Installation

```bash
npm install cache-redis-config
```

## Usage

```javascript
const RedisCache = require('cache-redis-config');

const redisCache = new RedisCache({
  host: '127.0.0.1',
  port: 6379,
  password: 'yourpassword',
  ttl: 3600 // Default TTL in seconds
});

redisCache.set('key', 'value')
  .then(() => redisCache.get('key'))
  .then(value => console.log(value)) // Output: 'value'
  .catch(err => console.error(err));
```

## Configuration Options

| Option    | Default      | Description                             |
|-----------|--------------|-----------------------------------------|
| `host`    | '127.0.0.1'  | Redis server host                       |
| `port`    | 6379         | Redis server port                       |
| `password`| null         | Password for authentication             |
| `ttl`     | 3600         | Default time-to-live for cache entries |

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)