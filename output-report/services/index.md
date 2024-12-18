# Services Migration Guide

## Overview

This guide provides an overview of the migration of Angular services to React. Services in Angular are often used for shared business logic, API calls, and storing application state, which will need to be adapted for React's architecture.

### Angular Services

- Discuss how services in Angular offer singleton instances for shared logic.
- Mention the use of dependency injection for accessing these services across components.

### React Migration Steps

- Explain transitioning from services to custom hooks for logic reuse and context for global state management.
- Highlight adapting Angular's RxJS observables to React, potentially using hooks for stateful operations.

### Challenges and Solutions

- Address the differences in dependency injection and how to mimic this pattern in React for shared logic.

### High-Level Architectural Changes

- Discuss the shift from service layers to hook-based logic encapsulation in React.

### Further Reading

- [Detailed Migration Documentation](./detailed-service-migration.md)

This summary outlines the general approach to migrating services, but detailed steps and examples can be found in the linked documentation.