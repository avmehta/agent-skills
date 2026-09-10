---
name: tradingview-chart-analysis
description: Analyze TradingView charts or watchlists for a clearly defined objective such as momentum, entry quality, support/resistance, supply/demand, or risk/reward, and optionally manage chart drawings. Use when the user asks for TradingView chart analysis or annotations. Do not use for trade execution or general portfolio management.
---

# TradingView Chart Analysis

Keep the analysis objective stable. Strong momentum, an attractive entry, and a high-confidence price level are different claims.

## Establish the objective

Infer it from the request or ask only when genuinely ambiguous:

- **Momentum:** relative strength, price trend, moving-average structure, volume, and candle persistence.
- **Entry quality:** momentum plus extension from moving averages, nearby resistance/support, consolidation quality, and invalidation distance.
- **Support/resistance:** repeated separated reactions and role reversals at a level.
- **Supply/demand:** zones where price left decisively and later reactions confirm an area rather than a single line.
- **Risk/reward:** entry, invalidation, likely target, and the uncertainty of each.

Do not rank “best momentum” as “best entry.” A strong chart can be too extended, and a favorite company can be pressing into major overhead resistance.

## Inspect consistently

1. Use the requested chart, watchlist, timeframe, indicators, and date range. If the visible range is only approximate, say so.
2. Read numerical series when available and visually inspect candles, gaps, wicks, bases, breakouts, failed moves, and reactions.
3. For multi-symbol work, apply the same criteria and date window to every symbol.
4. Treat indicator values as evidence, not the whole decision. Explain disagreements between indicators and price structure.
5. Separate observation from inference and state confidence.

## Drawings

- Preserve existing drawings unless the user explicitly asks to replace or clear them.
- Before bulk annotation, define consistent qualification and deduplication rules.
- Prefer a small set of well-tested levels over dense decoration when the user requests high confidence.
- After drawing, verify symbol, timeframe, price coordinates, style, count, and that existing objects remain intact.
- Save a screenshot or concise drawing ledger when useful for review.

## Reporting

Lead with the ranking or levels, then give the evidence that differentiates them. Include invalidation or “wait for” conditions when discussing entries. Avoid certainty language and do not execute trades unless the user separately requests an authorized trading workflow.

