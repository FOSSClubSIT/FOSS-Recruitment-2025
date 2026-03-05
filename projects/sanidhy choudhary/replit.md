# Overview

This is a real-time neuro-music application that generates adaptive music based on EEG brainwave data. The system monitors mental states (focus, arousal, valence) and dynamically adjusts musical parameters to enhance cognitive performance and well-being. Users can participate in solo sessions or collaborative "jam sessions" where multiple participants' neural activity influences the shared musical experience.

The application combines brain-computer interface technology with generative music, providing features like session tracking, achievement systems, analytics dashboards, and social collaboration tools for neurofeedback-enhanced experiences.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The frontend uses React with TypeScript, built on Vite for fast development and optimized builds. The UI is constructed with Radix UI components and styled using Tailwind CSS with a custom neural-themed design system. State management relies on TanStack Query for server state and React hooks for local state.

The component architecture is modular, with dedicated components for EEG visualization, music controls, session management, and social features. Real-time visualization is handled through HTML5 Canvas and Three.js for 3D brain rendering and particle effects.

## Backend Architecture
The server runs on Express.js with TypeScript, implementing a RESTful API alongside WebSocket connections for real-time features. The architecture separates concerns through dedicated modules for routing, storage abstraction, and WebSocket message handling.

The storage layer uses an abstract interface pattern with a memory-based implementation that can be easily swapped for database persistence. Session management, user data, EEG recordings, and jam session coordination are handled through this unified storage interface.

## Real-Time Communication
WebSocket connections enable live collaboration features including multi-user jam sessions, real-time EEG data streaming, and synchronized music parameter updates. The WebSocket server maintains connection pools organized by session and jam session IDs for efficient message routing.

## Audio Engine
The audio system is built on Tone.js, providing real-time audio synthesis with multiple instrument types (piano, pads, strings, percussion). The engine responds to mental state changes by adjusting tempo, harmony, complexity, and effects parameters. Audio generation is procedural and adaptive, creating unique musical experiences based on neural feedback.

## Data Schema Design
The database schema supports users, individual focus sessions, collaborative jam sessions, achievements, and EEG data storage. Mental state tracking includes arousal, valence, and focus metrics with timestamped progression. Music parameters are stored alongside neural data for session replay and analysis.

The schema accommodates both private individual sessions and public collaborative experiences, with participant management for jam sessions and achievement tracking for gamification.

# External Dependencies

## Database
- PostgreSQL via Neon Database (@neondatabase/serverless)
- Drizzle ORM for type-safe database operations and schema management
- Connection pooling and session storage through connect-pg-simple

## UI Framework
- React with TypeScript for component architecture
- Radix UI for accessible component primitives
- Tailwind CSS for utility-first styling
- Shadcn/ui component library for consistent design system

## Audio Processing
- Tone.js for real-time audio synthesis and effects
- Web Audio API for low-level audio manipulation and routing

## Data Fetching & State
- TanStack React Query for server state management and caching
- WebSocket API for real-time bidirectional communication

## 3D Visualization
- Three.js for 3D brain visualization and neural network rendering
- Canvas API for 2D EEG waveform displays and particle effects

## Build Tools
- Vite for fast development server and optimized production builds
- ESBuild for server-side bundling and compilation
- TypeScript for type safety across the entire application stack

## Development Environment
- Replit-specific plugins for runtime error handling and development tooling
- PostCSS with Autoprefixer for CSS processing