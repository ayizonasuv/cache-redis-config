export type RedisConfig = {
  host: string;
  port: number;
  password: string;
  database: number;
};

export type CacheConfig = {
  ttl: number;
  prefix: string;
  redis: RedisConfig;
};

export type CacheConfigObject = CacheConfig & {
  redis: RedisConfig & {
    url?: string;
  };
};