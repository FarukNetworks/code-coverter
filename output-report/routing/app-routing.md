# App Routing Module

- **File:** `app-routing.module.ts`
- **Description:** Defines the routes of the application.
- **Routes:**
  - Path: '', redirectTo: '/dashboard', pathMatch: 'full'
  - Path: 'dashboard', component: DashboardComponent
  - Path: 'login', component: LoginComponent

# Route Guards

- **AuthGuard**
  - **File:** `auth.guard.ts`
  - **Description:** Prevents navigation to certain routes for unauthenticated users.
- **ResolveGuard**
  - **File:** `stats-resolve.guard.ts`
  - **Description:** Pre-fetches statistical data before navigating to the Dashboard route.