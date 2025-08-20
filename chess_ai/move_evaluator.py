import openai
import chess

class MoveEvaluator:
    def __init__(self, model="gpt-5-mini"):
        self.model = model

    def evaluate_moves(self, fen, moves):
        moves_str = [move.uci() for move in moves]
        prompt = f"""
You are a world-class chess AI. Current position in FEN: {fen}
Legal moves: {moves_str}

Rate each move from 0 (worst) to 10 (best) and provide reasoning.
Return in the format:
move: score - explanation
"""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        text = response.choices[0].message.content
        return self.parse_response(text)

    def parse_response(self, text):
        # Parse GPT output into dictionary {move: score}
        move_scores = {}
        lines = text.splitlines()
        for line in lines:
            if ':' in line and '-' in line:
                move_part, rest = line.split(':', 1)
                score_part = rest.split('-', 1)[0].strip()
                try:
                    move_scores[move_part.strip()] = float(score_part)
                except:
                    continue
        return move_scores

    def best_move(self, fen, moves):
        scores = self.evaluate_moves(fen, moves)
        if not scores:
            return None
        best = max(scores, key=scores.get)
        return best, scores[best]
