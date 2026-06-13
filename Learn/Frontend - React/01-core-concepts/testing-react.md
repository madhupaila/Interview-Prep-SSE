# Testing React — RTL + MSW

---

## Philosophy

Test **what users see and do** — not implementation details.

```typescript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('submits login form', async () => {
  const user = userEvent.setup();
  render(<LoginPage />);
  await user.type(screen.getByLabelText(/email/i), 'a@b.com');
  await user.type(screen.getByLabelText(/password/i), 'secret');
  await user.click(screen.getByRole('button', { name: /sign in/i }));
  expect(await screen.findByText(/welcome/i)).toBeInTheDocument();
});
```

---

## MSW Setup

```typescript
import { setupServer } from 'msw/node';
import { http, HttpResponse } from 'msw';

const server = setupServer(
  http.post('/api/chat', () => HttpResponse.json({ ok: true }))
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

---

## What to Mock

| Mock | Don't mock |
|------|------------|
| API (MSW) | React itself |
| Router (MemoryRouter) | Simple presentational components |
| Date/time if flaky | User-visible text |

---

## Interview Script

> "RTL with getByRole and userEvent. MSW for network so tests match production fetch paths. renderHook for custom hooks. I avoid snapshot-only tests and testing useState directly."

---

## Related Questions

- [Q29 RTL best practices](../03-classic-react/questions/Q29-testing-library-best-practices.md)
- [Q30 MSW mocking](../03-classic-react/questions/Q30-mock-service-worker-react.md)
