#პროექტის აღწერა:
#პრობლემა: შექმენით პროგრამა, რომელიც დაამუშავებს სტუდენტების ქულების სიას და მოიძებნის მაქსიმალურ, მინიმალურ და საშუალო ქულას.
def process_scores(scores):
    if not scores:
        return "No scores available"

    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)

    return max_score, min_score, avg_score

# სტუდენტების ქულების სია
scores = [85, 90, 78, 92, 88, 76, 95, 89]

max_score, min_score, avg_score = process_scores(scores)

print(f"მაქსიმალური ქულა: {max_score}")
print(f"მინიმალური ქულა: {min_score}")
print(f"საშუალო ქულა: {avg_score:.2f}")
