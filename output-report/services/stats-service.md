# Stats Service

- **File:** `stats.service.ts`
- **Description:** Provides statistical data for the application.
- **Methods:**
  - `getStats()`: Returns an Observable containing stats data.
- **Decorators:** `@Injectable({ providedIn: 'root' })`
- **Observations:** Utilizes HttpClient for API requests.