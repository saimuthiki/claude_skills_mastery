---
name: designing-gamma-reference-architecture
description: |
  Reference architecture for enterprise Gamma integrations.
  Use when designing systems, planning integrations,
  or implementing best-practice Gamma architectures.
  Trigger with phrases like "gamma architecture", "gamma design",
  "gamma system design", "gamma integration pattern", "gamma enterprise".
allowed-tools: Read, Write, Edit
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Gamma Reference Architecture

## Overview
Reference architecture patterns for building scalable, maintainable Gamma integrations.

## Prerequisites
- Understanding of microservices
- Familiarity with cloud architecture
- Knowledge of event-driven systems

## Architecture Patterns

### Pattern 1: Basic Integration
```
┌─────────────────────────────────────────────────────────┐
│                    Your Application                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐             │
│  │   UI    │───▶│   API   │───▶│ Gamma   │             │
│  │         │    │ Server  │    │ Client  │             │
│  └─────────┘    └─────────┘    └────┬────┘             │
│                                      │                   │
└──────────────────────────────────────┼──────────────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │   Gamma API     │
                              └─────────────────┘
```

**Use Case:** Simple applications, prototypes, small teams.

### Pattern 2: Service Layer Architecture
```
set -euo pipefail
┌────────────────────────────────────────────────────────────────┐
│                         Your Platform                           │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  Web App │  │Mobile App│  │   CLI    │  │   API    │        │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│       │             │             │             │                │
│       └─────────────┴──────┬──────┴─────────────┘                │
│                            ▼                                     │
│                  ┌──────────────────┐                           │
│                  │ Presentation     │                           │
│                  │    Service       │                           │
│                  └────────┬─────────┘                           │
│                           │                                      │
│  ┌────────────────────────┼────────────────────────┐            │
│  │                        ▼                        │            │
│  │  ┌─────────┐  ┌─────────────┐  ┌─────────┐     │            │
│  │  │  Cache  │◀─│Gamma Client │──▶│  Queue  │     │            │
│  │  │ (Redis) │  │  Singleton  │  │ (Bull)  │     │            │
│  │  └─────────┘  └──────┬──────┘  └─────────┘     │            │
│  │                      │                          │            │
│  └──────────────────────┼──────────────────────────┘            │
│                         │                                        │
└─────────────────────────┼────────────────────────────────────────┘
                          ▼
                 ┌─────────────────┐
                 │   Gamma API     │
                 └─────────────────┘
```

**Use Case:** Multi-platform products, medium-scale applications.

### Pattern 3: Event-Driven Architecture
```
set -euo pipefail
┌─────────────────────────────────────────────────────────────────────┐
│                          Your Platform                               │
│                                                                      │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐             │
│  │  Producer   │    │  Producer   │    │  Consumer   │             │
│  │  Service    │    │  Service    │    │  Service    │             │
│  └──────┬──────┘    └──────┬──────┘    └──────▲──────┘             │
│         │                  │                  │                      │
│         └──────────────────┴──────────────────┘                      │
│                            │                                         │
│                   ┌────────▼────────┐                               │
│                   │  Message Queue   │                               │
│                   │   (RabbitMQ)     │                               │
│                   └────────┬─────────┘                               │
│                            │                                         │
│         ┌──────────────────┼──────────────────┐                     │
│         │                  ▼                  │                     │
│         │  ┌───────────────────────────────┐  │                     │
│         │  │    Gamma Integration Worker    │  │                     │
│         │  │  ┌─────────┐  ┌─────────────┐ │  │                     │
│         │  │  │ Handler │  │Gamma Client │ │  │                     │
│         │  │  └─────────┘  └──────┬──────┘ │  │                     │
│         │  └──────────────────────┼────────┘  │                     │
│         │                         │           │                     │
│         └─────────────────────────┼───────────┘                     │
│                                   │                                  │
└───────────────────────────────────┼──────────────────────────────────┘
                                    ▼
                           ┌─────────────────┐
                           │   Gamma API     │
                           │                 │◀──── Webhooks
                           └─────────────────┘
```

**Use Case:** High-volume systems, async processing, microservices.

## Implementation

### Service Layer Example
```typescript
// services/presentation-service.ts
import { GammaClient } from '@gamma/sdk';
import { Cache } from './cache';
import { Queue } from './queue';

export class PresentationService {
  private gamma: GammaClient;
  private cache: Cache;
  private queue: Queue;

  constructor() {
    this.gamma = new GammaClient({
      apiKey: process.env.GAMMA_API_KEY,
    });
    this.cache = new Cache({ ttl: 300 });  # 300: timeout: 5 minutes
    this.queue = new Queue('presentations');
  }

  async create(userId: string, options: CreateOptions) {
    // Add to queue for async processing
    const job = await this.queue.add({
      type: 'create',
      userId,
      options,
    });

    return { jobId: job.id, status: 'queued' };
  }

  async get(id: string) {
    return this.cache.getOrFetch(
      `presentation:${id}`,
      () => this.gamma.presentations.get(id)
    );
  }

  async list(userId: string, options: ListOptions) {
    return this.gamma.presentations.list({
      filter: { userId },
      ...options,
    });
  }
}
```

### Event Handler Example
```typescript
// workers/gamma-worker.ts
import { Worker } from 'bullmq';
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

const worker = new Worker('presentations', async (job) => {
  switch (job.data.type) {
    case 'create':
      const presentation = await gamma.presentations.create(job.data.options);
      await notifyUser(job.data.userId, 'created', presentation);
      return presentation;

    case 'export':
      const exportResult = await gamma.exports.create(
        job.data.presentationId,
        job.data.format
      );
      await notifyUser(job.data.userId, 'exported', exportResult);
      return exportResult;

    default:
      throw new Error(`Unknown job type: ${job.data.type}`);
  }
});
```

## Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| API Gateway | Auth, rate limiting, routing |
| Service Layer | Business logic, orchestration |
| Gamma Client | API communication, retries |
| Cache Layer | Response caching, deduplication |
| Queue | Async processing, load leveling |
| Workers | Background job execution |
| Webhooks | Real-time event handling |

## Resources
- [Gamma Architecture Guide](https://gamma.app/docs/architecture)
- [12-Factor App](https://12factor.net/)
- [Microservices Patterns](https://microservices.io/)

## Next Steps
Proceed to `gamma-multi-env-setup` for environment configuration.

## Instructions

1. Assess the current state of the design configuration
2. Identify the specific requirements and constraints
3. Apply the recommended patterns from this skill
4. Validate the changes against expected behavior
5. Document the configuration for team reference

## Output

- Configuration files or code changes applied to the project
- Validation report confirming correct implementation
- Summary of changes made and their rationale

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Authentication failure | Invalid or expired credentials | Refresh tokens or re-authenticate with design |
| Configuration conflict | Incompatible settings detected | Review and resolve conflicting parameters |
| Resource not found | Referenced resource missing | Verify resource exists and permissions are correct |

## Examples

**Basic usage**: Apply gamma reference architecture to a standard project setup with default configuration options.

**Advanced scenario**: Customize gamma reference architecture for production environments with multiple constraints and team-specific requirements.