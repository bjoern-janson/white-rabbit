# Operation-Relative Adequacy

> **RESEARCH BOUNDARY — FROZEN**

This note records the smallest mathematical boundary currently supported by the capability–correction lineage. It is not a new theory, experiment, or claim of general AI behavior.

## 1. Exact mathematical core

Let

```math
q:X\to Q
```

be a representation and

```math
e:X\to Y
```

an operation.

The operation is exactly representable from `Q` iff there exists

```math
\bar e:Q\to Y
```

such that

```math
\boxed{e=\bar e\circ q}.
```

Equivalently,

```math
\boxed{e\text{ descends through }q\iff \ker q\subseteq\ker e.}
```

Every distinction collapsed by `q` must also be irrelevant to `e`.

Adequacy is therefore operation-relative, not an intrinsic property of a representation.

For an operation family `\mathcal O`, define

```math
x\sim_{\mathcal O}y
\iff
\forall e\in\mathcal O,\ e(x)=e(y).
```

If

```math
\mathcal O_t\subseteq\mathcal O_{t+1},
```

then

```math
\boxed{\sim_{\mathcal O_{t+1}}\subseteq\sim_{\mathcal O_t}.}
```

A representation may therefore be adequate when constructed and become inadequate for a later operation without itself changing.

### Native exact operation contract

For a fixed representation `q`, define its exact operation contract as

```math
\boxed{
\mathcal O_q
=
\{e:\ker q\subseteq\ker e\}.
}
```

This is the family of exact operations that can be realized without recovering distinctions discarded by `q`.

For an operation outside `\mathcal O_q`, the possibilities are not exhausted by representation failure. The operation may instead require:

```text
additional retained structure
reconstruction
external reacquisition
approximation
or failure
```

Therefore preserve the methodological rule:

```math
\boxed{\text{failure to factor}\neq\text{causal diagnosis}.}
```

Failure to factor identifies an incompatibility between the declared operation and the retained representation. It does not by itself identify why that incompatibility arose or why the operation is unavailable in practice.

## 2. Hard boundary on unrestricted future adequacy

If the admissible future operation family can distinguish every pair of distinct states, then

```math
\bigcap_{e\in\mathcal O_{\rm all}}\ker e=\Delta_X.
```

Under exact fidelity and with no external reacquisition, any retained representation `r` that must support every such future operation must satisfy

```math
\ker r=\Delta_X,
```

so `r` must be injective.

```math
\boxed{
\text{unrestricted future distinctions}
+
\text{exact fidelity}
+
\text{no reacquisition}
\Rightarrow
\text{injective retention}
}
```

This rules out a nontrivial exact compression that discards distinctions while guaranteeing compatibility with every conceivable future distinguishing operation.

The scientifically interesting question is therefore restricted:

```math
\boxed{
\textbf{What restrictions on the future operation family permit useful compression while preserving cheap refinement?}
}
```

## 3. Lower boundary: the state space itself may already be inadequate

The factorization result assumes the consequential operation is expressible on `X`.

To expose that assumption, distinguish the world from the constructed state space:

```math
\boxed{W\xrightarrow{p}X\xrightarrow{q}Q.}
```

Let

```math
e^\star:W\to Y
```

be a consequential operation defined at the world level.

The first question is whether there exists

```math
\tilde e:X\to Y
```

such that

```math
e^\star=\tilde e\circ p.
```

Equivalently:

```math
\ker p\subseteq\ker e^\star.
```

If

```math
\boxed{\ker p\not\subseteq\ker e^\star,}
```

then some `w_1,w_2` satisfy

```math
p(w_1)=p(w_2)
```

while

```math
e^\star(w_1)\neq e^\star(w_2).
```

The distinction is absent from the constructed state space itself. No downstream refinement of `q` can recover it from `X` alone.

```math
\boxed{
\textbf{Factorization can preserve or recover a distinction only given a state space in which that distinction exists.}
}
```

This is the current lower boundary of the result. Interface/state-space discovery remains OPEN.

## 4. Diagnostic order

Keep the failure loci separate:

```math
\boxed{
\text{state-space}
\rightarrow
\text{representation}
\rightarrow
\text{factorization}
\rightarrow
\text{recovery}
\rightarrow
\text{resource reachability}
\rightarrow
\text{intervention}
\rightarrow
\text{validation}
}
```

Ask, in order:

1. **Does the relevant operation exist on `X`?**
2. **What representation actually survived?**
3. **Does the operation descend through that representation?**
4. **If not directly, can the missing distinction be reconstructed or reacquired through an independently available channel?**
5. **Is that realization reachable within the declared resources, access conditions, and interface?**
6. **If reachable, can it legitimately alter the operative system when intervention is required?**
7. **If altered, does the result survive independent validation?**

These questions are not interchangeable.

When an operation fails or appears unavailable, competing native explanations can include:

```text
state-space construction
representation loss
recovery failure
resource limit
access failure
intervention failure
implementation defect
```

The factorization test does not choose among these causes automatically.

In particular:

```text
factorization != intelligence
factorization != corrigibility
factorization != interface discovery
factorization != reachability
factorization != authority
factorization != validation
```

## 5. Synthetic empirical anchor

The dormant-recoverability experiment held the operative compressed representation fixed between two conditions:

```text
C = compressed operative representation only
D = identical operative representation + inactive dormant recovery structure
```

Present computation was identical, while future structural correction cost differed:

```math
\boxed{
\text{same present computation}
+
\text{different recovery structure}
\Rightarrow
\text{different future correction cost}
}
```

The bounded empirical claim is therefore not that compression generally harms correction. It is that present operational equivalence need not imply future correction equivalence, and non-operative retained structure can change that future correction boundary under a declared intervention language.

See `dormant-recoverability-v0.1/RESULT.md` for the experiment-specific claim ceiling.

## 6. External engineering specimen — optimized debugging

Optimized debugging provides independent engineering pressure on the same distinction without adopting this vocabulary.

A production representation may remain adequate for ordinary execution while later source-level debugging operations fall into native classes such as:

```text
directly realizable
requires retained/reconstructed debug structure
unavailable / optimized out
```

LLVM and GDB independently implement mechanisms for retaining mappings, reconstructing values, and explicitly withholding unsupported source-level values rather than fabricating them.

This is supporting external evidence, not a proof that compiler optimization is literally the quotient map above. The safe construction is operation-local:

```math
X=\text{source-level states relevant to a particular operation}
```

and

```math
q:X\to Q=\text{information actually available at the optimized observation point}.
```

Then ask, operation by operation, whether the native operation factors through what is available or requires additional retained/reconstructed structure.

Useful native references:

- LLVM, *Source Level Debugging with LLVM*: https://llvm.org/docs/SourceLevelDebugging.html
- LLVM, *InstrRef Debug Info*: https://llvm.org/docs/InstrRefDebugInfo.html
- LLVM, *How to Update Debug Info*: https://llvm.org/docs/HowToUpdateDebugInfo.html
- GDB, *Print Settings / entry values*: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Print-Settings.html

The external specimen is deliberately not promoted beyond this consistency check.

## 7. Frozen boundary

Preserve these two questions above the bench:

```math
\boxed{\textbf{Does the operation exist on }X\textbf{ at all?}}
```

```math
\boxed{\textbf{If it exists, does it descend through what survived?}}
```

The factorization result governs what happens once the consequential operation is expressible in the constructed state space.

The unsolved frontier begins one layer earlier:

```math
\boxed{
\textbf{How does consequence induce construction of a distinction that the current state space cannot express?}
}
```

**OPEN.**

## 8. Adversarial portability phase

The next phase is not to accumulate confirming analogies.

```math
\boxed{\textbf{DON'T PROVE PORTABILITY. TRY TO DESTROY IT.}}
```

For a mature external system, preserve its native terminology and select a real operation that the system independently has reason to support. Then ask:

```text
What operation is actually promised or required?
What representation actually survived?
Does that operation factor through what survived?
If not, what native recovery or reacquisition path exists?
If the operation remains unavailable, what is the native causal explanation?
```

The highest-value adversarial specimen is one where an operation initially appears not to factor through the retained representation, but native evidence shows that the actual failure lies elsewhere—for example in access, resources, intervention machinery, state-space construction, or implementation.

A confirming example is lower-value than a case that forces the diagnostic instrument to sharpen or admit a boundary.

The objective is therefore not:

```text
Where else does this framework fit?
```

It is:

```math
\boxed{\textbf{Where does this instrument stop working?}}
```

Do not extend this note by vocabulary alone. Reopen it only under a real operation class, an external counterexample, or a failure that forces revision.
